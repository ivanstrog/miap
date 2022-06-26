import './App.css';
import Main from "./components/Main";
import { StyledEngineProvider } from '@mui/material/styles';

function App() {
    return (
        <div className="App">
            <div className='container'>
                <StyledEngineProvider injectFirst>
                    <Main/>
                </StyledEngineProvider>
            </div>
        </div>
    );
}

export default App;
