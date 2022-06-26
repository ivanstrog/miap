import { createStore} from "redux";

const defaultState = {
    page: 'main',
    cart: []
}

const reducer = (state = defaultState, action) => {
    switch (action.type) {
        case "cart":
            return {...state, cart: action.payload};
        case "page":
            return {...state, page: action.payload};
        default:
            return state;
    }
};

export const NavigationStateStore = createStore(reducer);