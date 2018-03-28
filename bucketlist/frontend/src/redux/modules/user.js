// imports

// actions

const SAVE_TOKEN = "SAVE_TOKEN";
const LOGOUT = "LOGOUT";


// action creators

function saveToken(token) {
    return {
        type: SAVE_TOKEN,
        token
    };
}

function logout() {
    return {
        type: LOGOUT
    };
}


// API actions

function usernameLogin(username, password) {
    return dispatch => {
        fetch("/api-token-auth/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        })
            .then(response => response.json())
            .then(json => {
                if (json.token) {
                    dispatch(saveToken(json.token));
                }
            })
            .catch(err => console.log(err));
    };
}

// initial state

const initialState = {
    isLoggedIn: localStorage.getItem("jwt") ? true : false,
    token: localStorage.getItem("jwt")
};

// reducer
function reducer(state = initialState, action) {
    switch (action.type) {
        case SAVE_TOKEN:
            return applySetToken(state, action);
        case LOGOUT:
            return applyLogout(state, action); 
        default:
            return state;
    }
}
// reducer functions
function applySetToken(state, action) {
    const { token } = action;
    localStorage.setItem("jwt", token);
    return {
        ...state,
        isLoggedIn: true,
        token: token
    };
}
function applyLogout(state, action) {
    localStorage.removeItem("jwt");
    return {
        isLoggedIn: false
    };
}
// exports
const actionCreators = {
    usernameLogin,
    logout,
};

export { actionCreators };

// export reducer by default

export default reducer;