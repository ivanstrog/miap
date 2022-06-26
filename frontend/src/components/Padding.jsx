function Padding({children}) {
    let w_width = 0
    if (typeof window !== 'undefined') {
        w_width = window.innerWidth;
    }

    return <div style={{
        paddingLeft: `calc(max(50vw - 500px, 32px))`,
        paddingRight: `calc(max(50vw - 500px, 32px))`,
    }}>
        {children}
    </div>
}

export default Padding;