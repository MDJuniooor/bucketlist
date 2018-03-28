import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as userActions } from "../../redux/modules/user";

const mapStateToProps = (state, ownProps) => {
    const { user } = state;
    return {
        isLoggedIn: user.isLoggedIn,
    };
};
const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        logout: ()=> {
            dispatch(userActions.logout());
        },

    };
};
export default connect(mapStateToProps, mapDispatchToProps)(Container);
