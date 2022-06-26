import Card from "./Card";
import {useEffect, useState} from "react";
import {click} from "@testing-library/user-event/dist/click";
import {CircularProgress, Skeleton} from "@mui/material"

function concat_(str) {
    let s = ''
    for (let i in str) {
        s += str[i];
        s += '#';
    }
    return s.substr(0, Math.max(s.length - 1, 0));
}

function packer_(mp) {
    let res = {time: '', category: '',  resource: '', company_name: ''};
    res["time"] = mp["time"];
    res["category"] = concat_(mp["category"]);
    res["resource"] = concat_(mp["resource"]);
    res["company_name"] = concat_(mp["company_name"]);
    return res;
}

function News({state, setState, clicked}) {

    useEffect(() => {
        console.log(packer_(state));
    }, [state]);

    useEffect(() => {
        console.log('Clicked');
    }, [clicked]);


    return true ? <div style={{marginTop: '0px', width: '70%', marginLeft: '32px'}}>
        {/*<CircularProgress/>*/}
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
        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>
        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

        <Card category='Edsfjdlksfjlkds' company_name={'dsfdsfdsfdsf'} date={'dsfdsfds'} link={'dsffffffffffff'}
              title={'dsffffffffffffff'}/>

    </div>
}

export default News;