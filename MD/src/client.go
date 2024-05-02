package main

import (
	"bufio"
	"encoding/gob"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
	"sync"
)

var ClientWG sync.WaitGroup

func parse_input(input string) Request {

    split_input := strings.Split(input, " ")

    if split_input[0] == "close" {
        return Request{ Req_type: "close" }
    }

    if len(split_input) < 3 {
        log.Println("Not enough arguments provided to for a request.")
        return Request{}
    }

    return Request{
        Req_type: split_input[1],
        Endpoint: Endpoint(split_input[2]),
        Payload: RequestInfo{
            Parameters: split_input[3:],
            Collection: split_input[0],
        },
    }
}

func start_client() {
	conn, err := net.Dial("tcp", "localhost:" + fmt.Sprint(PORT))
	scanner := bufio.NewScanner(os.Stdin)
	encoder := gob.NewEncoder(conn)

	if err != nil {
		log.Println("An error occurred when trying to connect to socket:", err)
	}

	defer conn.Close()

	for {

		fmt.Println("** REQUEST FORMAT -> COLLECTION_NAME GET ENDPOINT PARAMETERS (*OPTIONAL*) ... **")
		fmt.Println("Insert new request information:")

		if !scanner.Scan() {
			// Error or EOF encountered
			if err := scanner.Err(); err != nil {
				log.Println("Error reading input:", err)
			}
			return
		}

		input := scanner.Text()
		request := parse_input(input)
		err := encoder.Encode(request)

		if err != nil {
			log.Println(err)
			return
		}
	}
}

func run_client() {
	ClientWG.Add(1)
	start_client()
	ClientWG.Wait()
}
