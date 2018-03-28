import React, { Component } from "react";
import "./style.scss";

class Footer extends Component {
    render() {
        return (
            <div className="Footer">
                <div className="Logo"><h1>DRIVE</h1></div>
                <h1>We are <strong>inspired</strong> by others</h1>
                <h2>Visualize your dream and kick your bucketlists!</h2>
                <ul className="Icons">
                    <li className="Icon"><i className="icono-facebook"></i></li>
                    <li className="Icon"><i className="icono-instagram"></i></li>
                </ul>
            </div>
        );
    }
}

export default Footer;