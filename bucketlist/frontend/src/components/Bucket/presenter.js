import React from 'react';
import LinesEllipsis from 'react-lines-ellipsis';
import Ionicon from "react-ionicons";
import './style.scss';

const Bucket = props => {

    return (
        <div className="Bucket">
            <div className="Bucket__Column1">
                <div className="centered">
                    <img src={props.file} alt={props.file} />
                </div>
            </div>

            <div className="Bucket__Column2">
                <span className="Like" onClick={props.handleHeartClick}>
                    {props.is_liked ? (
                        <Ionicon icon="ios-battery-full" fontSize="1.8em" color="#581078" />
                    ) : (
                            <Ionicon icon="ios-battery-dead" fontSize="1.8em" color="black" />
                        )}
                </span>
                <h1>{props.location}</h1>
                <div className="Bucket__Genres">
                    <h1>{props.like_count} supporters</h1>
                </div>
                <div className="Bucket__Synopsis">
                    <LinesEllipsis
                        text={props.caption}
                        maxLine='2'
                        ellipsis='...'
                        trimRight
                        basedOn='letters'
                    />
                </div>
            </div>
        </div>
    )
}
export default Bucket