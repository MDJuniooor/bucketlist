import React, { Component } from "react";
import Bucket from "./presenter";

// TODO: If the user is logged in, call API
class Container extends Component {

    render() {
        return <Bucket {...this.props} {...this.state} />;
    }
}

export default Container;
