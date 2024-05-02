############################################################################################
##																						  ##
##                                  ENVIRONMENT VARIABLES                                 ##
##																						  ##
############################################################################################
SOURCES = $(wildcard src/*.go)
############################################################################################

build_server: 
	@go build -o bin/md $(SOURCES)

build_client: 
	@go build -o bin/client $(SOURCES)

build: build_server build_client

run_server: build
	@./bin/md 

run_client: build
	@./bin/client 

race_server:
	@go run --race $(SERVER_SOURCES)

clean:
	rm -rf bin/

