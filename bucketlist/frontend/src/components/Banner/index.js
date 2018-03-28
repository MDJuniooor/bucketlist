import React, { Component } from 'react';
import './style.scss';
import Slider from 'react-slick';

function NextArrow(props) {
    const { className, style, onClick } = props
    return (
        <div
            className={className}
            style={{
                ...style,
                zIndex: 100,
                position: 'absolute',
                display: 'block',
                background: 'transparent'
            }}
            onClick={onClick}></div>
    );
}

function PrevArrow(props) {
    const { className, style, onClick } = props
    return (
        <div
            className={className}
            style={{
                ...style,
                zIndex: 100,
                position: 'absolute',
                display: 'block',
                background: 'transparent'
            }}
            onClick={onClick}>
        </div>
    );
}

class Banner extends Component {
    render() {
        const settings = {
            dots: true,
            infinite: true,
            speed: 1000,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            nextArrow: <NextArrow />,
            prevArrow: <PrevArrow />
        };
        return (
            <div className="Container">
                <Slider {...settings}>
                    <div className="Content"><img className="BannerImage" src={window.location.origin + '/images/1.jpg'} alt="artist" /></div>
                    <div className="Content"><img className="BannerImage" src={window.location.origin + '/images/2.jpg'} alt="artist" /></div>
                </Slider>
            </div>
        );
    }
}


export default Banner
