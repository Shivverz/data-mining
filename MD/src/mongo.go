package main

import (
	"context"
	"fmt"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
)

var client *mongo.Client
var database *mongo.Database

const DB_NAME = "sportmonks"

func connect_to_mongo() {
	MONGO_URI := "mongodb://localhost:27017"
	clientOption := options.Client().ApplyURI(MONGO_URI)

    var err error
    client, err = mongo.Connect(context.Background(), clientOption)
	if err != nil {
		log.Fatal(err)
	}

	err = client.Ping(context.Background(), nil)
	if err != nil {
		log.Fatal(err)
	}

	database = client.Database(DB_NAME)
	fmt.Println("Successfully connected to MongoDB on " + DB_NAME + " database!")
}

func save_to_database(data []interface{}, collection_name string) {
	collection := database.Collection(collection_name)

	_, err := collection.InsertMany(context.Background(), data)
	if err != nil {
		log.Fatal(err)
	}
}
