#include "variaveis.cpp"
#include "funcoes.cpp"

enum SampleSizes {
	SAMPLE_SIZE_1 = 100,
	SAMPLE_SIZE_2 = 1000,
	SAMPLE_SIZE_3 = 10000,
};




enum SortValues {
	BUBBLE_SORT, SAMPLE_1, ARQUITETURA = 0,
	MERGE_SORT, SAMPLE_2, TIPO = 1,
	QUICK_SORT, SAMPLE_3, QTD_RAM = 2,
	QTD_NUCLEOS = 3
};




int main() {
	std::vector<std::string> hardwareInfo;
	GetWindowsHardwareInfo(hardwareInfo);

	std::vector<std::vector<std::string>> specs;

	int lastLine;
	int id = 1;

	// FUNCAO USADA PARA CRIAR A POPULACAO
	// std::vector<float> pop;
	// CreatePopulation(pop);
	// Print(pop);

	// Variaveis das amostras
	std::vector<float> sample1;
	std::vector<float> sample2;
	std::vector<float> sample3;

	// Header do csv
	std::vector<std::string> sample1RunTime;
	std::vector<std::string> sample2RunTime;
	std::vector<std::string> sample3RunTime;

	// Geração das amostras
	GenerateSample(sample1, population, SAMPLE_SIZE_1);
	GenerateSample(sample2, population, SAMPLE_SIZE_2);
	GenerateSample(sample3, population, SAMPLE_SIZE_3);


	std::vector<std::string> header = { "TAM AMOSTRA", "TEMPO", "SPECS_ID" };
	std::vector<std::vector<std::string>> results;

	lastLine = GetCSVPos("../results/specs.csv");

	if (lastLine == 0) {
		specs.push_back({ "ID", "SO", "ARQUITETURA DA CPU", "TIPO DA CPU", "QTD NUCLEOS", "QTD RAM" });
	}

	if (!IsSpecsInCSV("../results/specs.csv", id, GetOSName(), hardwareInfo.at(ARQUITETURA), hardwareInfo.at(TIPO), hardwareInfo.at(QTD_NUCLEOS), hardwareInfo.at(QTD_RAM))) {
		specs.push_back({ std::to_string(id), GetOSName(), hardwareInfo.at(ARQUITETURA), hardwareInfo.at(TIPO), hardwareInfo.at(QTD_NUCLEOS), hardwareInfo.at(QTD_RAM) });
	}

	// Exportacao para csv
	ExportToCSV(specs, "../results/specs.csv");

	for (int i = 0; i < 1000; i++) {
		RunBubbleSortAndShowResults(sample1, 1, sample1RunTime);
		RunBubbleSortAndShowResults(sample2, 2, sample2RunTime);
		RunBubbleSortAndShowResults(sample3, 3, sample3RunTime);

		lastLine = GetCSVPos("../results/bubble.csv");

		if (lastLine == 0) {
			results.push_back(header);
		}

		results.push_back({ std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(BUBBLE_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(BUBBLE_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(BUBBLE_SORT), std::to_string(id) });

		// Exportacao para csv
		ExportToCSV(results, "../results/bubble.csv");

		results.clear();

		RunMergeSortAndShowResults(sample1, 1, sample1RunTime);
		RunMergeSortAndShowResults(sample2, 2, sample2RunTime);
		RunMergeSortAndShowResults(sample3, 3, sample3RunTime);

		lastLine = GetCSVPos("../results/merge.csv");

		if (lastLine == 0) {
			results.push_back(header);
		}

		results.push_back({ std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(MERGE_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(MERGE_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(MERGE_SORT), std::to_string(id) });

		// Exportacao para csv
		ExportToCSV(results, "../results/merge.csv");

		results.clear();

		RunQuickSortAndShowResults(sample1, 1, sample1RunTime);
		RunQuickSortAndShowResults(sample2, 2, sample2RunTime);
		RunQuickSortAndShowResults(sample3, 3, sample3RunTime);

		lastLine = GetCSVPos("../results/quick.csv");

		if (lastLine == 0) {
			results.push_back(header);
		}

		results.push_back({ std::to_string(SAMPLE_SIZE_1), sample1RunTime.at(QUICK_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_2), sample2RunTime.at(QUICK_SORT), std::to_string(id) });
		results.push_back({ std::to_string(SAMPLE_SIZE_3), sample3RunTime.at(QUICK_SORT), std::to_string(id) });

		// Exportacao para csv
		ExportToCSV(results, "../results/quick.csv");

		results.clear();
	}

	return EXIT_SUCCESS;
}