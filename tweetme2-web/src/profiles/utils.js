
import React from 'react' // since DisplayCount is used as functional component

import numeral from 'numeral'

export function DisplayCount(props){
    return <span className={props.className}>{numeral(props.children).format("0a")}</span>
}