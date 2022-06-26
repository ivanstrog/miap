import Padding from "./Padding";
import Filters from "./Filters";
import News from "./News";
import Toolbar from "./Toolbar";
import {useEffect, useState} from "react";

function Main() {

    const [state, setState] = useState({time: [], category: [],  resource: [], company_name: []});
    const [clicked, setIsClicked] = useState(false);

    return <Padding>
        <Toolbar/>

        <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'flex-start',
        }}>
            <Filters state={state} setState={setState} setIsClicked={setIsClicked} clicked={clicked}/>
            <News state={state} setState={setState} clicked={clicked}/>
        </div>
    </Padding>
}

export default Main;