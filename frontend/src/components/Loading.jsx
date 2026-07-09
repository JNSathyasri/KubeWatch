import Spinner from "react-bootstrap/Spinner";

function Loading() {
    return (
        <div className="loading">
            <Spinner animation="border" variant="primary" />
        </div>
    );
}

export default Loading;