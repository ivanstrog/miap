function Toolbar() {
    return <>
        <>
            {/*<div style={{display: "flex", width: '50%'}}>*/}
            {/*    <div>NMBITS</div>*/}
            {/*</div>*/}
            <div style={{
                display: "flex",
                width: '100%',
                justifyContent: 'space-between',
                fontWeight: '300',
                cursor: 'pointer',
                paddingTop: '24px',
                paddingBottom: '24px',
                alignItems: 'center',
                textAlign: 'center'
            }}>
                <div style={{fontSize: '26px', fontWeight: '700', color: '#0D69F2'}}>МИАП</div>
                <div style={{display: 'flex', fontWeight: '500', color: '#6c6c70'}}>
                    <div style={{marginLeft: '62px'}}>Новости</div>
                    <div style={{marginLeft: '62px'}}>О системе</div>
                    <div style={{marginLeft: '62px'}}>+7 (911) 111 27 39</div>
                </div>
                <div style={{
                    fontWeight: '700',
                    border: 'solid 2px #6c6c70', borderRadius: '50%', width: '40px', height: '40px',
                    textAlign: 'center', justifyContent: 'center', display: 'flex', alignItems: 'center'
                }}>ИГ
                </div>
            </div>
        </>
    </>
}

export default Toolbar;