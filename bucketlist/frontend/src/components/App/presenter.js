import React from "react";
import { Route, Switch, withRouter } from "react-router-dom";
import Header from '../Header';
import Banner from '../Banner';
import Footer from '../Footer';
import BucketBox from '../BucketBox';
import Auth from '../Auth';

import "./styles.scss";

class App extends React.Component {
    render() {
        return (
            <div>
            <Header />
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route exact path="/howtouse" component={Home} />
                    <Route exact path="/enroll" component={Home} />
                    <Route exact path="/login" component={Auth} />
                </Switch>
            <Footer />
            </div>
        );
    }
}

const Home = props => (
    <div>
        <Banner />
        <BucketBox/>
    </div>
);

export default withRouter(App);
