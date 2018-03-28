import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as bucketActions } from '../../redux/modules/bucket';

const mapStateToProps = (state, ownProps) => {
    const { buckets: { bucket } } = state;
    return {
        bucket
    };
};
const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        getBucket: () => {
            dispatch(bucketActions.getBucket());
        }
    };
};
export default connect(mapStateToProps, mapDispatchToProps)(Container);
