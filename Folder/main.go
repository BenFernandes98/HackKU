// main package will always be executed first like main in C/C++
package main

// Import standard libraries
import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"
	"io/ioutil"

	// Mux is the best golang webserver that is very
	// simple to configure. You have to install it locally
	// before using
	// Run `go get -u github.com/gorilla/mux`
	"github.com/gorilla/mux"
	// cors library is needed for initializing a handler,
	// Ren `go get -u github.com/rs/cors` to install
	"github.com/rs/cors"
)

// Some global variable to store names and data
// from previous requests. Serve later
var (
	// allNames storing all names globally
	// You can use mutexes to ensure data integrity
	allNames1 []string = make([]string, 0, 16)
	// allNames2 []string = make([]string, 0, 16)
	// scores []string = make([]string, 0, 16)
)

func main() {
	// Create a new router to start receiving requests
	r := mux.NewRouter()
	// Handler gives us more control over timeouts
	handler := cors.Default().Handler(r)
	// Define the server
	srv := &http.Server{
		Handler: handler,
		Addr:    ":2020",
		// Good practice: enforce timeouts for servers you create!
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
		IdleTimeout:  60 * time.Second,
	}

	// Routes
	// Go to the functions' definitions to see the comments
	r.HandleFunc("/", root).Methods(http.MethodGet)
	r.HandleFunc("/random", random).Methods(http.MethodGet)
	r.HandleFunc("/name/{name}", name).Methods(http.MethodGet)
	r.HandleFunc("/sum", sum).Methods(http.MethodGet)
	r.HandleFunc("/submit", submit).Methods(http.MethodPost)
	r.HandleFunc("/get", get).Methods(http.MethodGet)
	r.HandleFunc("/display", display).Methods(http.MethodGet)

	// Let it run
	log.Println("Starting the server...")
	// Listen and serve until it errors out or dies
	if err := srv.ListenAndServe(); err != nil {
		log.Println(err)
	}
}

// Simple root path, just equivalent of "hello, world"
func root(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", "hello, world")
}

// Some constant paths to have steady routes
func random(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", fmt.Sprintf("Your random integer is %d", rand.Int31()))
}

// Cornhub function
func display(w http.ResponseWriter, r *http.Request) {
	result, err := ioutil.ReadFile("server/result.txt")
	if err != nil {
		fmt.Fprintf(w, "%s", "File reading error", err)
		return
	}
	rating := string(result)
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", rating)
	// //convert rating to int if possible
	// intRating, err := strconv.Atoi(rating)
	// if err != nil {
	// 	w.WriteHeader(http.StatusTeapot)
	// 	fmt.Fprintf(w, "%s", "Error occured while converting rating to int: "+err.Error())
	// 	return
	// }
	// if intRating < 50 {
	// 	fmt.Fprintf(w, "%s", "</3" + "INSULT HERE")
	// }	else {
	// 	fmt.Fprintf(w, "%s", "<3")
	// }
}

// Variable routes and paths where people can have a unique path
func name(w http.ResponseWriter, r *http.Request) {
	name := mux.Vars(r)["name"]
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", "Hello, "+name+"!")
}

// Path with request parameters and parsing
func sum(w http.ResponseWriter, r *http.Request) {
	// Get the query parameters path?a=...&b=...
	a := r.URL.Query().Get("a")
	b := r.URL.Query().Get("b")
	// Check if all values were parsed
	if a == "" || b == "" {
		w.WriteHeader(http.StatusTeapot)
		fmt.Fprintf(w, "%s", "a or b was not given")
		return
	}
	// Convert a and b to integers and check if that's possible
	aNum, err := strconv.Atoi(a)
	if err != nil {
		w.WriteHeader(http.StatusTeapot)
		fmt.Fprintf(w, "%s", "Error occured while converting a to int: "+err.Error())
		return
	}
	bNum, err := strconv.Atoi(b)
	if err != nil {
		w.WriteHeader(http.StatusTeapot)
		fmt.Fprintf(w, "%s", "Error occured while converting b to int: "+err.Error())
		return
	}
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", "a+b="+strconv.Itoa(aNum+bNum))
}

// This is the object we are receiving in our POST requests from submit
type userName struct {
	Name1 string `json:"name1"`
	Name2 string `json:"name2"`
	Score string `json:"score"`
}

// Submit receives the post request and adds a name
func submit(w http.ResponseWriter, r *http.Request) {
	name := &userName{}
	json.NewDecoder(r.Body).Decode(name)
	allNames1 = append(allNames1, name.Name1)
	allNames1 = append(allNames1, name.Score)
	allNames1 = append(allNames1, name.Name2)
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", "success")
}

// Get just returns results
func get(w http.ResponseWriter, r *http.Request) {
	output, _ := json.Marshal(allNames1)
	// output2, _ :=json.Marshal(allNames2)
	// output3, _ :=json.Marshal(scores)
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", output)
	// fmt.Fprintf(w, "%s", ",")
	// fmt.Fprintf(w, "%s", output2)
	// fmt.Fprintf(w, "%s", ",")
	// fmt.Fprintf(w, "%s", output3)
}
