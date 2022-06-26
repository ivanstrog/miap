import Card from "./Card";
import {useEffect, useState} from "react";
import {Skeleton} from "@mui/material"
import {get_news_by_filters} from "./api";

function concat_(str) {
    let s = ''
    for (let i in str) {
        s += str[i];
        s += '$';
    }
    return s.substr(0, Math.max(s.length - 1, 0));
}

function packer_(mp) {
    let res = {time: '', category: '', resource: '', company_name: ''};
    res["time"] = mp["time"];
    res["category"] = concat_(mp["category"]);
    res["resource"] = concat_(mp["resource"]);
    res["company_name"] = concat_(mp["company_name"]);
    return res;
}

function contains(a, obj) {
    let i = a.length;
    while (i--) {
        if (a[i] === obj) {
            return true;
        }
    }
    return false;
}

function News({state, setState, clicked}) {

    const [response, setResponse] = useState({});
    const [arc, setArc] = useState([]);
    const [tm, setTm] = useState(999999999);

    useEffect(() => {
        console.log(contains(arc, 62));
    }, [arc]);

    useEffect(() => {
        console.log(packer_(state));
        try {
            setTm(state['time'].getTime() / 1000);
        } catch (e) {
            setTm(999999999);
        }
    }, [state]);

    useEffect(() => {
        setResponse({})
        console.log('Clicked');
        get_news_by_filters(packer_(state)).then((response) => {
            response.json().then(r => {
                setResponse(r);
                console.log('get news success!');
            });
        }).catch((e) => {
            console.log(e);
            setResponse({})
        });
    }, [clicked]);

    useEffect(() => {
        console.log("HI");
        console.log(response['series']);
    }, [response]);


    return response['series'] === undefined ? <div style={{marginTop: '0px', width: '70%', marginLeft: '32px'}}>
        <Skeleton variant="rectangular" height={240}
                  style={{borderRadius: '12px', width: '70% !important', marginBottom: '16px',}}/>
        <Skeleton variant="rectangular" height={240}
                  style={{borderRadius: '12px', width: '70% !important', marginBottom: '16px',}}/>
        <Skeleton variant="rectangular" height={240}
                  style={{borderRadius: '12px', width: '70% !important', marginBottom: '16px',}}/>
    </div> : <div style={{
        minHeight: '300px',
        width: '70%',
        // background: '#ffffff',
    }}>
        {
            response['series'].map((elem, index) => {
                return (contains(arc, elem['id']) || tm > elem['date']) ? null :
                    <Card
                        key={index}
                        category={elem['category']}
                        company_name={elem['company_name']}
                        date={elem['date']}
                        link={elem['link']}
                        id={elem['id']}
                        title={elem['title']}
                        setArc={setArc}
                        arc={arc}
                    />
            })
        }


    </div>
}

export default News;