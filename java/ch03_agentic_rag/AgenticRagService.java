import java.util.ArrayList;
import java.util.List;

public class AgenticRagService {
    private final List<String> toolNames = List.of("search", "calendar", "database");

    public List<String> decideTools(String query) {
        if (query.toLowerCase().contains("calendar")) {
            return List.of("calendar");
        }
        return List.of("search");
    }

    public String run(String query) {
        List<String> retrieved = new ArrayList<>();
        retrieved.add("Document chunk A");
        retrieved.add("Document chunk B");

        List<String> toolOutputs = new ArrayList<>();
        for (String tool : decideTools(query)) {
            toolOutputs.add("Tool " + tool + " executed for: " + query);
        }

        return "Answer for query: " + query + "\nRetrieved context: " + retrieved + "\nTools: " + toolOutputs;
    }
}
