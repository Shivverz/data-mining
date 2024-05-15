package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var client *mongo.Client
var database *mongo.Database

const DB_NAME = "sportmonks"

func connect_to_mongo() {
    var err error

    err = godotenv.Load()

    if err != nil {
        log.Fatal("Error loading .env file")
    }

    mongoUser := os.Getenv("MONGO_USER")
    mongoPassword := os.Getenv("MONGO_PASSWORD")

	MONGO_URI := fmt.Sprintf("mongodb+srv://%s:%s@datamining.ywf7foj.mongodb.net/?retryWrites=true&w=majority&appName=DataMining", mongoUser, mongoPassword)
	clientOption := options.Client().ApplyURI(MONGO_URI)

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
