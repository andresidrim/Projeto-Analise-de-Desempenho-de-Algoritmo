#include "variaveis.cpp"
#include "funcoes.cpp"

enum SampleSizes {
	SAMPLE_SIZE_1 = 100,
	SAMPLE_SIZE_2 = 1000,
	SAMPLE_SIZE_3 = 10000,
};

enum SortValues {
	BUBBLE_SORT, SAMPLE_1 = 0,
	MERGE_SORT, SAMPLE_2 = 1,
	QUICK_SORT, SAMPLE_3 = 2
};

int main() {
	std::vector<std::string> hardwareInfo;
	GetWindowsHardwareInfo(hardwareInfo);

	std::cout << hardwareInfo.at(0) << "\n" << hardwareInfo.at(1) << "\n" << hardwareInfo.at(2) << "\n" << hardwareInfo.at(3) << std::endl;

	std::cout << GetOSName() << std::endl;

	int lastLine = GetCSVPos("results/output.csv");

	// FUNCAO USADA PARA CRIAR A POPULACAO
	// std::vector<float> populations;
	// CreatePopulation(populations);
	// Print(populations);

	// std::cout << "tam: " << population.size();

	// Variaveis das amostras
	std::vector<float> sample1;
	std::vector<float> sample2;
	std::vector<float> sample3;

	// Colunas do csv
	std::vector<std::string> col = { "ORDENAÇÃO", "TAM AMOSTRA", "TEMPO" };
	std::vector<std::string> row = { "BUBBLE SORT", "MERGE SORT", "QUICK SORT" };
	std::vector<std::string> sample1RunTime;
	std::vector<std::string> sample2RunTime;
	std::vector<std::string> sample3RunTime;

	std::vector<std::vector<std::string>> results;

	// Geração das amostras
	GenerateSample(sample1, population, SAMPLE_SIZE_1);
	GenerateSample(sample2, population, SAMPLE_SIZE_2);
	GenerateSample(sample3, population, SAMPLE_SIZE_3);


	if (lastLine == 0) {
		results.push_back(col);
	}

	RunBubbleSortAndShowResults(sample1, 1, sample1RunTime);
	RunBubbleSortAndShowResults(sample2, 2, sample2RunTime);
	RunBubbleSortAndShowResults(sample3, 3, sample3RunTime);

	results.push_back({ row.at(SAMPLE_1), std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(BUBBLE_SORT) });
	results.push_back({ row.at(SAMPLE_1), std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(BUBBLE_SORT) });
	results.push_back({ row.at(SAMPLE_1), std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(BUBBLE_SORT) });

	RunMergeSortAndShowResults(sample1, 1, sample1RunTime);
	RunMergeSortAndShowResults(sample2, 2, sample2RunTime);
	RunMergeSortAndShowResults(sample3, 3, sample3RunTime);

	results.push_back({ row.at(SAMPLE_2), std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(MERGE_SORT) });
	results.push_back({ row.at(SAMPLE_2), std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(MERGE_SORT) });
	results.push_back({ row.at(SAMPLE_2), std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(MERGE_SORT) });

	RunQuickSortAndShowResults(sample1, 1, sample1RunTime);
	RunQuickSortAndShowResults(sample2, 2, sample2RunTime);
	RunQuickSortAndShowResults(sample3, 3, sample3RunTime);

	results.push_back({ row.at(SAMPLE_3), std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(QUICK_SORT) });
	results.push_back({ row.at(SAMPLE_3), std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(QUICK_SORT) });
	results.push_back({ row.at(SAMPLE_3), std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(QUICK_SORT) });

	// Exportacao para csv
	ExportToCSV(results, "results/output.csv");

	return EXIT_SUCCESS;
}