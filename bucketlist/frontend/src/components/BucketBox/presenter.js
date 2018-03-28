import React from 'react';
import Bucket from '../Bucket';

const BucketBox = props => {
    if (props.loading) {
        return <LoadingBucket />;
    } else if (props.bucket) {
        return <RenderBucket {...props} />;
    }
};
const LoadingBucket = props => (
    <div>
        <h1>loading</h1>
    </div>
);

const RenderBucket = props => (
    <div>
        {props.bucket.map(bucket => <Bucket {...bucket} key={bucket.id} />)}
    </div>
);

export default BucketBox;