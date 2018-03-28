import { combineReducers, createStore, applyMiddleware } from "redux";
import { routerReducer, routerMiddleware } from "react-router-redux";
import { composeWithDevTools } from "redux-devtools-extension";
import createHistory from "history/createBrowserHistory";
import thunk from "redux-thunk";
import { i18nState } from "redux-i18n";
import buckets from './modules/bucket';
import user from './modules/user';

const env = process.env.NODE_ENV;

const history = createHistory(); // 히스토리 생성

const middlewares = [thunk, routerMiddleware(history)]; // 미들웨어에 히스토리 추가

if (env === "development") {
    const { logger } = require("redux-logger");
    middlewares.push(logger);
}

const reducer = combineReducers({
    user,
    buckets,
    routing: routerReducer, // 리듀서 생성
    i18nState
});

let store;

if (env === "development") {
    store = initialState =>
        createStore(
            reducer,
            composeWithDevTools(applyMiddleware(...middlewares))
        );
} else {
    store = initialState => createStore(reducer, applyMiddleware(...middlewares));
}
export { history };

export default store();
