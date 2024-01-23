#include "SimpleWeb/server.hpp"

int main() {
    WebServer server(8080);    // create a new webserver object to run at port 8080
    server.serve("html/");    // run the webserver at a certain directory
    
    return 0;
}