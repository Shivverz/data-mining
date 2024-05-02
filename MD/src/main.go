package main

import (
	"fmt"
	"os"
)

func main() {
    fmt.Println("Welcome to the Data Mining App!")
    switch os.Args[0] {
    case "./bin/md":
        run_server()    
        break

    case "./bin/client":
        run_client()
        break
    default:
        fmt.Println("Unknown executable name found:", os.Args[0])
    }
}
