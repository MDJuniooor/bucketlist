import React, { Component }  from "react";
import App from "./presenter";

// TODO: If the user is logged in, call API

class Container extends Component {
    state = {
        loading: true
    };
    
    render() {
 
        return <App {...this.state} />;
    }
}

export default Container;
