function StatusBadge({ value }) {

    const badgeColor =
        value === "Running"
            ? "success"
            : value === "Pending"
            ? "warning"
            : value === "Failed"
            ? "danger"
            : "secondary";

    return (
        <span className={`badge bg-${badgeColor}`}>
            {value}
        </span>
    );
}

export default StatusBadge;