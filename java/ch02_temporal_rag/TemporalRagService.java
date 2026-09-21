import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class TemporalRagService {
    private final List<TemporalDocument> documents = new ArrayList<>();

    public void addDocument(TemporalDocument doc) {
        documents.add(doc);
    }

    public List<TemporalDocument> retrieve(String query, LocalDate asOf, int topK) {
        return documents.stream()
            .map(doc -> new ScoredDocument(doc, score(query, doc, asOf)))
            .sorted(Comparator.comparingDouble(ScoredDocument::score).reversed())
            .limit(topK)
            .map(ScoredDocument::document)
            .toList();
    }

    private double score(String query, TemporalDocument doc, LocalDate asOf) {
        double semantic = query.toLowerCase().contains(doc.getText().toLowerCase()) ? 1.0 : 0.0;
        double recency = Math.max(0.0, 1.0 - (double) Math.abs(asOf.toEpochDay() - doc.getCreatedAt().toEpochDay()) / 365.0);
        return semantic + recency;
    }
}

record TemporalDocument(String text, LocalDate createdAt, String version) {
    public String getText() { return text; }
    public LocalDate getCreatedAt() { return createdAt; }
}

record ScoredDocument(TemporalDocument document, double score) {
    public double score() { return score; }
    public TemporalDocument document() { return document; }
}
