import React, {Component} from "react";
import Header from "./presenter";

// TODO: If the user is logged in, call API

class Container extends Component {
    render(){
        return(
            <Header
                {...this.props}
                handlelogout={this._handlelogout}
            />
        )
    }
    _handlelogout = response => {
        console.log(this.props);
        const { logout } = this.props;
        logout();
    };

}

export default Container;