import React, { Component } from "react";
import Auth from "./presenter";

class Container extends Component {
    state = {
        action: "login"
    };
    render() {
        const { action } = this.state;
        return <Auth action={action} />;
    }
}

export default Container;
