import React, { Component } from "react";
import PropTypes from "prop-types";
import BucketBox from "./presenter";

// TODO: If the user is logged in, call API

class Container extends Component {
    state = {
        loading: true
    };
    static propTypes = {
        getBucket: PropTypes.func.isRequired,
        bucket: PropTypes.array
    };
    componentDidMount() {
        const { getBucket} = this.props;
 

        if (!this.props.bucket) {
            getBucket();
        } else {
            this.setState({
                loading: false
            });
        }
    }
    componentWillReceiveProps = nextProps => {
        if (nextProps.bucket) {
            this.setState({
                loading: false
            });
        }
    };
    render() {
        const { bucket } = this.props;
        
        return <BucketBox {...this.state} bucket={bucket} />;
    }
}

export default Container;
