import React, { Component } from "react";
import { Link } from 'react-router-dom';
import "./Header.css";

class Header extends Component {
    
    render() {
        const {isLoggedIn} = this.props;
        console.log(isLoggedIn);
        return (
            <div className="Header">
                <div className="Logo"><h1>DRIVE</h1></div>
                <ul className="Menu">
                    <li className="MenuBtn"><Link to="/howtouse">사용방법</Link></li>
                    <li className="MenuBtn"><Link to="/enroll">버킷등록</Link></li>
                    
                    {(isLoggedIn) ? 
                        <li className="MenuBtn" onClick={this.props.handlelogout}><Link to='/'>로그아웃</Link></li>
                     : <li className="MenuBtn"><Link to="/login">로그인</Link></li>}
                </ul>
            </div>
        );
    }
}

export default Header;