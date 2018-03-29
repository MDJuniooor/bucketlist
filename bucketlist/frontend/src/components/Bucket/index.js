import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as bucketActions } from '../../redux/modules/bucket';

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        handleHeartClick: () => {
            if (ownProps.is_liked) {
                dispatch(bucketActions.unlikeBucket(ownProps.id));
            } else {
                dispatch(bucketActions.likeBucket(ownProps.id));
            }
        }
    };
};

export default connect(null, mapDispatchToProps)(Container);