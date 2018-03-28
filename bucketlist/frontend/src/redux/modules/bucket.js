// imports

import { actionCreators as userActions } from "./user";

// actions

const SET_BUCKET = "SET_BUCKET";
const LIKE_BUCKET = "LIKE_BUCKET";
const UNLIKE_BUCKET = "UNLIKE_BUCKET";

// action creators

function setBucket(bucket) {
    return{
        type: SET_BUCKET,
        bucket
    };
}

function doLikeBucket(bucketId){
    return{
        type: LIKE_BUCKET,
        bucketId
    }
}

function doUnLikeBucket(bucketId) {
    return{
        type: UNLIKE_BUCKET,
        bucketId
    }
}
// API actions

function getBucket(){
    return(dispatch, getState) => {
        const { user: { token } } = getState();
        fetch("/buckets/",{
            method: "GET",
            headers: {
                Authorization: `JWT ${token}`
            }
        })
    .then(response => {
        return response.json();
    })
    .then(json => {
        dispatch(setBucket(json));
    });
    }
}

function likeBucket(bucketId) {
    return(dispatch, getState) => {
        dispatch(doLikeBucket(bucketId));
        const {user:{token}}= getState();
        fetch(`/buckets/${bucketId}/likes/`,{
            method: "POST",
            headers: {
                Authorization: `JWT ${token}`
            }
        })
        .then(response => {
            if(response.status === 401){
                dispatch(userActions.logout());
            } else if(!response.ok){
                dispatch(unlikeBucket(bucketId));
            }
        });
    }
}

function unlikeBucket(bucketId) {
    return(dispatch, getState) => {
        dispatch(doUnLikeBucket(bucketId));
        const { user: {token}} = getState();
        fetch(`/buckets/${bucketId}/unlikes/`,{
            method: "DELETE",
            headers:{
                Authorization: `JWT ${token}`
            }
        }).then(response => {
            if(response.status === 401) {
                dispatch(userActions.logout());
            }else if (!response.ok){
                dispatch(doLikeBucket(bucketId));
            }
        });
    }
}
// initial state

const initialState = {};


// reducer

function reducer(state = initialState, action) {
    
    switch (action.type) {
        case SET_BUCKET:
            return applySetBucket(state, action);
        case LIKE_BUCKET:
            return applyLikeBucket(state, action);
        case UNLIKE_BUCKET:
            return applyUnLikeBucket(state, action);
        default:
            return state;
    }
}

// reducer functions

    function applySetBucket(state, action) {
        const { bucket } = action;
        return {
            ...state,
            bucket
        };
    }

    function applyLikeBucket(state, action) {
        const { bucketId } = action;
        const { bucket } = state;
        const updatedBucket = bucket.map(bucket => {
            if(bucket.id ===bucketId){
                return { ...bucket, is_liked: true, like_count: bucket.like_count+1};
            }
            return bucket;
        });
        return {...state, bucket: updatedBucket};
    }

    function applyUnLikeBucket(state, action) {
        const { bucketId } = action;
        const { bucket } = state;
        const updatedBucket = bucket.map(bucket => {
            if (bucket.id === bucketId) {
                return { ...bucket, is_liked: false, like_count: bucket.like_count - 1 };
            }
            return bucket;
        });
        return { ...state, bucket: updatedBucket };
    }
// exports

const actionCreators = {
    getBucket,
    likeBucket,
    unlikeBucket
};

export { actionCreators};
// export reducer by default

export default reducer;