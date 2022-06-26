import StickyBox from "react-sticky-box";

import * as React from 'react';
import TextField from '@mui/material/TextField';
import {AdapterDateFns} from '@mui/x-date-pickers/AdapterDateFns';
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider';
import {DatePicker} from '@mui/x-date-pickers/DatePicker';
import {useTheme} from '@mui/material/styles';
import Box from '@mui/material/Box';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Chip from '@mui/material/Chip';
import _without from "lodash/without";
import {Button} from "@mui/material";
import {useEffect} from "react";

//--------------------------------------------------------Date----------------------------------------------------------

function BasicDatePicker_({state, setState, operation}) {
    const [value, setValue] = React.useState(null);
    useEffect(() => {
        if (state !== undefined) {
            let mp = {...state};
            console.log(state);
            mp[operation] = value
            setState(mp);
        }
    }, [value])

    return (
        <LocalizationProvider dateAdapter={AdapterDateFns}>
            <DatePicker
                label="Новости начиная с даты"
                value={value}
                onChange={(newValue) => {
                    setValue(newValue);
                }}
                renderInput={(params) => <TextField {...params} style={{width: '300px'}}/>}
            />
        </LocalizationProvider>
    );
}

//--------------------------------------------------------Tags----------------------------------------------------------

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
    PaperProps: {
        style: {
            maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
            width: 250,
        },
    },
};

const names = [
    'Инновации',
    'Патент',
    'Импортзамещение',
    'Научные разработки',
    'Гранты',
    'Исследования',
    'Технологии'
];

function getStyles(name, personName, theme) {
    return {
        fontWeight:
            personName.indexOf(name) === -1
                ? theme.typography.fontWeightRegular
                : theme.typography.fontWeightMedium,
    };
}

function MultipleSelectChip_({label, items, state, setState, operation}) {


    const theme = useTheme();
    const [personName, setPersonName] = React.useState([]);

    useEffect(() => {
        let mp = {...state};
        mp[operation] = personName
        setState(mp);
    }, [personName])

    const handleChange = (event) => {
        const {
            target: {value},
        } = event;
        setPersonName(
            // On autofill we get a stringified value.
            typeof value === 'string' ? value.split(',') : value,
        );
    };


    const handleDelete = (event, value) => {
        event.preventDefault();
        setPersonName((current) => _without(current, value));
        // setState(personName);
        let mp = {...state};
        mp[operation] = personName
        setState(mp);
    };

    return (
        <div>
            <FormControl sx={{width: 300}}>
                <InputLabel id="demo-multiple-chip-label">{label}</InputLabel>
                <Select
                    labelId="demo-multiple-chip-label"
                    id="demo-multiple-chip"
                    multiple
                    value={personName}
                    onChange={handleChange}
                    style={{borderColor: '#0D69F2'}}
                    input={<OutlinedInput id="select-multiple-chip" label={label}/>}
                    renderValue={(selected) => (
                        <Box sx={{display: 'flex', flexWrap: 'wrap', gap: 0.5, zIndex: '2092130'}}>
                            {selected.map((value) => (
                                <Chip style={{background: '#F1F2F4'}} key={value} label={value} onMouseDown={(event) => {
                                    event.stopPropagation();
                                }}
                                      onDelete=
                                          {(event) => handleDelete(event, value)}/>
                            ))}
                        </Box>
                    )}
                    MenuProps={MenuProps}
                >
                    {items.map((name) => (
                        <MenuItem
                            key={name}
                            value={name}
                            style={getStyles(name, personName, theme)}
                        >
                            {name}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
        </div>
    );
}

function Filters({state, setState, setIsClicked, clicked}) {
    return <>
        <StickyBox offsetTop={20} offsetBottom={20}>
            <div className={'filters'} style={{
                width: '400px',
                background: '#ffffff',
                minHeight: '300px',
                borderRadius: '12px',
                justifyContent: 'start',
                display: 'flex',
                flexDirection: 'column',
                paddingLeft: '16px',
                paddingTop: '16px',
                textAlign: 'left',
            }}>
                <div style={{marginBottom: '16px', fontWeight: '500px', fontSize: '20px'}}>Показать с выбранной даты
                </div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <BasicDatePicker_ state={state} setState={setState} operation={'time'}/>
                </div>
                <div style={{marginBottom: '16px', fontWeight: '500px', fontSize: '20px'}}>Категории инвестиционной
                    активности
                </div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <MultipleSelectChip_ items={names} label={'Теги'} state={state} setState={setState} operation={'category'}/>
                </div>
                <div style={{marginBottom: '16px', fontWeight: '500px', fontSize: '20px'}}>Источники</div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <MultipleSelectChip_ items={names} label={'Ссылки на источники'} state={state} setState={setState} operation={'resource'}/>
                </div>
                <div style={{marginBottom: '16px', fontWeight: '500px', fontSize: '20px'}}>Предприятия</div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <MultipleSelectChip_ items={names} label={'Ссылки на источники'} state={state} setState={setState} operation={'company_name'}/>
                </div>
                <Button
                    variant="contained"
                    style={{
                        marginBottom: '16px',
                        width: '300px',
                        cursor: 'pointer',
                        border: 'none',
                        background: '#0D69F2',
                        color: 'white',
                        padding: '8px',
                        textAlign: 'center',
                        alignItems: 'center',
                        borderRadius: '12px',
                        justifyContent: 'center',
                        fontSize: '16px',
                        textTransform: 'none'
                    }}
                    onClick={() => {setIsClicked(!clicked)}}
                >
                    Применить
                </Button>
            </div>
            <div className={'filters'} style={{
                width: '400px',
                background: '#ffffff',
                borderRadius: '12px',
                justifyContent: 'start',
                display: 'flex',
                flexDirection: 'column',
                paddingLeft: '16px',
                paddingTop: '16px',
                marginTop: '16px',
                textAlign: 'start',
            }}>
                <div style={{marginBottom: '16px', fontWeight: '500px', fontSize: '20px'}}>Экспортировать как</div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <BasicDatePicker_/>
                </div>
                <div style={{display: 'flex', marginBottom: '16px'}}>
                    <Button variant="contained" style={{
                        cursor: 'pointer',
                        border: 'none',
                        background: '#0D69F2',
                        color: 'white',
                        padding: '8px',
                        textAlign: 'center',
                        width: '70px',
                        alignItems: 'center',
                        borderRadius: '12px',
                        justifyContent: 'center'
                    }}>.XLS
                    </Button>
                    <Button variant="contained" style={{
                        marginLeft: '16px',
                        cursor: 'pointer',
                        border: 'none',
                        background: '#0D69F2',
                        color: 'white',
                        padding: '8px',
                        textAlign: 'center',
                        width: '70px',
                        alignItems: 'center',
                        borderRadius: '12px',
                        justifyContent: 'center'
                    }}>.DOCX
                    </Button>
                </div>
            </div>
        </StickyBox>
    </>
}

export default Filters;