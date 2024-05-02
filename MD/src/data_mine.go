package main

import (
	"encoding/gob"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"net"
	"net/http"
	"strings"
	"sync"
)

const (
	API_TOKEN    = "LzTcv7co5Bs45YFGOcuCeVVS0oSVvP3OQmxQp29G8UVA9Nw8l3p1ZF9PZ7Vv"
	URL          = "https://api.sportmonks.com/v3/football/"
	RES_PER_PAGE = "&per_page=50"
	PAGE         = "&page="
	PORT         = 9090
)

var WG sync.WaitGroup

/**
*      ************************************************
*      *                                              *
*      *                App Custom Types              *
*      *                                              *
*      ************************************************
**/
type RequestInfo struct {
	Parameters []string
    Collection string
}

type Endpoint string

type Request struct {
	Req_type string
	Endpoint Endpoint
	Payload  RequestInfo
}

/**
*      *******************************************************************
*      *                                                                 *
*      *                 Connection and Request Handling                 *
*      *                                                                 *
*      *******************************************************************
*
 */
func build_request_url(endpoint Endpoint, parameters []string, page_number uint32) string {
	concat_param := ""

	for _, param := range parameters {
		concat_param = concat_param + "&" + param
	}

	return URL + string(endpoint) + "?api_token=" + API_TOKEN + concat_param + PAGE + fmt.Sprint(page_number) + RES_PER_PAGE
}

func parse_response_body(body []byte, collection_name string) (string, error) {

	var response_body map[string]interface{}
	err := json.Unmarshal(body, &response_body)

	if err != nil {
		log.Println("An error occurred when trying to parse the response body information:", err)
		return "", err
	}

	if message, ok := response_body["message"]; ok {
		log.Println("Bad request detected:", message)
		return "", errors.New("Bad request detected.")
	}

	pagination, ok := response_body["pagination"].(map[string]interface{})
	if !ok {
		log.Println("Pagination key not found or has unexpected type!")
		return "", errors.New("Pagination key not found or has unexpected type!")
	}

	next_request_url, ok := pagination["next_page"].(string)
	if !ok {
		log.Println("Next Page key not found or has unexpected type!")
		return "", errors.New("Next Page key not found or has unexpected type!")
	}

	rate_limit, ok := response_body["rate_limit"].(map[string]interface{})
	if !ok {
		log.Println("Rate Limit key not found or has unexpected type!")
		return "", errors.New("Rate Limit key not found or has unexpected type!")
	}

	remaining_tokens, ok := rate_limit["remaining"].(float64)
	if !ok {
		log.Println("Remaining key not found or has unexpected type!")
		return "", errors.New("Remaining key not found or has unexpected type!")
	}

	if remaining_tokens == 0.0 || next_request_url == "null" {
		return "", errors.New("No more requests are available")
	}

	data, ok := response_body["data"].([]interface{})
	if !ok {
		log.Println("Data key not found or has unexpected type!")
		return "", errors.New("Data key not found or has unexpected type!")
	}

	// fmt.Println(data)
	save_to_database(data, collection_name)

	return next_request_url, nil
}

func make_request(client *http.Client, request_url string, page_request chan string, collection_name string) {
	method := "GET"
	req, err := http.NewRequest(method, request_url, nil)

	if err != nil {
		log.Println(err)
		return
	}

	res, err := client.Do(req)

	if err != nil {
		log.Println(err)
		return
	}

	defer res.Body.Close()

	body, err := io.ReadAll(res.Body)

	next_request_url, err := parse_response_body(body, collection_name)

	// Whenever we reach the last request page or exhaust the number of credits we stop the request flow
	if err != nil {
		close(page_request)
		return
	}

    split_req := strings.Split(next_request_url, "?")
    next_request_url = split_req[0] + "?api_token=" + API_TOKEN + "&" + split_req[1]

    go func() {
        page_request <- next_request_url
    }()
}

func handle_request(request Request, starting_page uint32) {
	request_url := build_request_url(request.Endpoint, request.Payload.Parameters, starting_page)
	var page_requests = make(chan string)

	client := http.Client{}

	go func() {
		page_requests <- request_url
	}()

	for req_url := range page_requests {
		make_request(&client, req_url, page_requests, request.Payload.Collection)
	}
}

func handle_connection(conn net.Conn) {
	defer conn.Close()
	decoder := gob.NewDecoder(conn)

	for {
		var request Request
		err := decoder.Decode(&request)

		if err != nil {
			log.Println(err)

			if err == io.EOF {
				return
			}

			continue
		}

		switch request.Req_type {
		case "get":
			fmt.Println(request)
			go handle_request(request, 1)
			break

		case "close":
			return

		default:
			fmt.Println("Unknown request type found: " + request.Req_type)
			break
		}
	}
}

/**
*      ************************************************
*      *                                              *
*      *                 Server Setup                 *
*      *                                              *
*      ************************************************
**/
func start_server() {
	listerner, err := net.Listen("tcp4", "127.0.0.1:"+fmt.Sprint(PORT))

	if err != nil {
		log.Println(err)
	}

	defer listerner.Close()

	for {
		conn, err := listerner.Accept()

		if err != nil {
			log.Println(err)
			continue
		}

		go handle_connection(conn)
	}
}

func run_server() {
	WG.Add(1)
	start_server()
	WG.Wait()
}
