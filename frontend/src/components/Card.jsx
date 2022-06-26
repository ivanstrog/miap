import {Button} from "@mui/material";

function Card({company_name, date, resource, title, link, category}) {
    return <div style={{
        marginLeft: '16px',
        background: '#ffffff',
        borderRadius: '12px',
        marginBottom: '16px',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'left',
        alignItems: 'flex-start',
        padding: '16px',
        textAlign:'left',
    }}>
        <button
            color="error"
            style={{
            background: 'transparent',
            color: '#de3401',
            fontWeight: '600',
            border: 'none',
            marginRight: '0',
            marginLeft: 'auto',
            marginBottom: '-16px',
            cursor: 'pointer',
                textTransform: 'none',
        }}>В архив</button>
        <div style={{marginBottom: '14px', color: '#062757', fontWeight: '600', alignItems: 'flex-start'}}>{company_name}</div>
        <div style={{
            width: '100%',
            fontSize: '20px',
            fontWeight: '600',

        }}>{title}
        </div>
        <div style={{marginBottom: 0, marginTop: 'auto', width: '100%'}}>
            <Button  variant="outlined" size="small" style={{
                textTransform: 'none',
                marginTop: '16px',
                borderColor: '#0D69F2',
                color: '#0D69F2',
                // fontWeight: '600'
            }}>{link.substr(0, 30) + '...'}</Button>
            <hr color={'#c4c4c4'} style={{background: '#c4c4c4'}}/>
            <div style={{display: 'flex', justifyContent: 'space-between', width: '100%'}}>
                <div>{'#' + category}</div>
                <div>{date} </div>
            </div>
        </div>
    </div>
}

export default Card;