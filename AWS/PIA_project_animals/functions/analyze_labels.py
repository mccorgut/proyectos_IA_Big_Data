def analyze_labels(labels):
    try:
        # Count the number of detected labels
        total_labels = len(labels)

        # Calculate the average confidence score across all labels
        avg_confidence = (
            sum(label["Confidence"] for label in labels) / total_labels
            if total_labels > 0 else 0  # Handle case where no labels are detected
        )

        # Filter labels with confidence scores greater than 90%
        high_confidence_labels = [
            label["Name"] for label in labels if label["Confidence"] > 90
        ]

        # Return the analysis results as a dictionary
        return {
            "total_labels": total_labels,                # Total number of labels detected
            "average_confidence": avg_confidence,        # Average confidence score
            "high_confidence_labels": high_confidence_labels  # List of high-confidence labels
        }
    except Exception as e:
        # Raise an exception with an error message if something goes wrong
        raise Exception(f"Error analyzing labels: {e}")
