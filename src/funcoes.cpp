#pragma once

#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <string>
#include <fstream>
#include <cmath>

#ifdef _WIN32
#include <Windows.h>
#include <VersionHelpers.h>

std::string GetOSName() {
  return "Windows";
}

int GetWindowsHardwareInfo(std::vector<std::string> &hardwareInfo) {
  SYSTEM_INFO sysInfo;
  GetSystemInfo(&sysInfo);

  MEMORYSTATUSEX memoryStatus;
  memoryStatus.dwLength = sizeof(memoryStatus);

  switch (sysInfo.wProcessorArchitecture) {
  case PROCESSOR_ARCHITECTURE_AMD64:
    hardwareInfo.push_back("x64");
    break;
  case PROCESSOR_ARCHITECTURE_INTEL:
    hardwareInfo.push_back("x86");
    break;
  default:
    std::cerr << "Architecture not found\n";
    return EXIT_FAILURE;
  }

  switch (sysInfo.dwProcessorType) {
  case PROCESSOR_INTEL_386:
    hardwareInfo.push_back("INTEL 386");
    break;
  case PROCESSOR_INTEL_486:
    hardwareInfo.push_back("INTEL 486");
    break;
  case PROCESSOR_INTEL_PENTIUM:
    hardwareInfo.push_back("INTEL PENTIUM");
    break;
  case PROCESSOR_INTEL_IA64:
    hardwareInfo.push_back("INTEL IA64");
    break;
  case PROCESSOR_AMD_X8664:
    hardwareInfo.push_back("AMD64");
    break;
  default:
    std::cerr << "CPU type not found\n";
    return EXIT_FAILURE;
  }

  if (GlobalMemoryStatusEx(&memoryStatus)) {
    hardwareInfo.push_back(std::to_string(memoryStatus.ullTotalPhys / (1024 * 1024)) + " MB");
  }
  else {
    std::cerr << "Falha ao obter informações de memória." << std::endl;
    return EXIT_FAILURE;
  }

  hardwareInfo.push_back(std::to_string(sysInfo.dwNumberOfProcessors));


  return EXIT_SUCCESS;
}

#elif __APPLE__
#include <sys/types.h>
#include <sys/sysctl.h>

std::string GetOSName() {
  return "MacOS";
}

int GetMacHardwareInfo(std::vector<std::string> &hardwareInfo) {
  // Processor Architecture
  const char *arch = nullptr;
  size_t len = 0;
  if (sysctlbyname("hw.machine", nullptr, &len, nullptr, 0) == 0) {
    arch = new char[len];
    sysctlbyname("hw.machine", (void *)arch, &len, nullptr, 0);
    hardwareInfo.push_back(arch);
    delete[] arch;
  }
  else {
    std::cerr << "Architecture not found\n";
    return EXIT_FAILURE;
  }

  // Processor Type
  int type;
  len = sizeof(type);
  if (sysctlbyname("hw.cputype", &type, &len, nullptr, 0) == 0) {
    switch (type) {
    case CPU_TYPE_X86:
      hardwareInfo.push_back("x86");
      break;
    case CPU_TYPE_X86_64:
      hardwareInfo.push_back("x64");
      break;
    default:
      std::cerr << "CPU type not found\n";
      return EXIT_FAILURE;
    }
  }
  else {
    std::cerr << "CPU type not found\n";
    return EXIT_FAILURE;
  }

  // Memory
  int mib[2];
  mib[0] = CTL_HW;
  mib[1] = HW_MEMSIZE;
  int64_t size = 0;
  len = sizeof(size);
  if (sysctl(mib, 2, &size, &len, nullptr, 0) == 0) {
    hardwareInfo.push_back(std::to_string(size / (1024 * 1024)));
  }
  else {
    std::cerr << "Failed to get memory information." << std::endl;
    return EXIT_FAILURE;
  }

  // Number of Processors
  int cpuCount;
  len = sizeof(cpuCount);
  if (sysctlbyname("hw.logicalcpu", &cpuCount, &len, nullptr, 0) == 0) {
    hardwareInfo.push_back(std::to_string(cpuCount));
  }
  else {
    std::cerr << "Failed to get CPU information." << std::endl;
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}

#elif __LINUX__
#include <sstream>

std::string GetOSName() {
  return "Linux";
}

int GetLinuxHardwareInfo(std::vector<std::string> &hardwareInfo) {
  // Processor Architecture
  std::ifstream archFile("/proc/cpuinfo");
  std::string line;
  while (std::getline(archFile, line)) {
    if (line.find("architecture") != std::string::npos) {
      size_t pos = line.find(":");
      if (pos != std::string::npos) {
        hardwareInfo.push_back(line.substr(pos + 2)); // Assuming the architecture information follows ": "
        break;
      }
    }
  }
  archFile.close();

  // Processor Type
  std::ifstream cpuFile("/proc/cpuinfo");
  while (std::getline(cpuFile, line)) {
    if (line.find("model name") != std::string::npos) {
      size_t pos = line.find(":");
      if (pos != std::string::npos) {
        hardwareInfo.push_back(line.substr(pos + 2)); // Assuming the model name information follows ": "
        break;
      }
    }
  }
  cpuFile.close();

  // Memory
  std::ifstream memFile("/proc/meminfo");
  while (std::getline(memFile, line)) {
    if (line.find("MemTotal") != std::string::npos) {
      std::istringstream iss(line);
      std::string token, value;
      iss >> token >> value;
      hardwareInfo.push_back(value);
      break;
    }
  }
  memFile.close();

  // Number of Processors
  int cpuCount = std::thread::hardware_concurrency();
  if (cpuCount > 0) {
    hardwareInfo.push_back(std::to_string(cpuCount));
  }
  else {
    std::cerr << "Failed to get CPU information." << std::endl;
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}

#endif

// FUNCOES //
void Print(const std::vector<float> &sample) {
  std::cout << "[ ";

  for (int i = 0; i < sample.size(); i++) {
    i != sample.size() - 1 ? std::cout << sample.at(i) << ", " : std::cout << sample.at(i);
  }

  std::cout << " ]" << std::endl;
}

void CreatePopulation(std::vector<float> &population) {
  std::random_device rd;
  std::mt19937 gen(rd());

  std::uniform_real_distribution<float> dist(0.0, 20000.0);

  for (int i = 0; i < 20000; i++) {
    float randomNumber = dist(gen);
    population.push_back(randomNumber);
  }
}

void GenerateSample(std::vector<float> &sample, std::vector<float> population, int sampleSize) {
  std::random_device rd;
  std::mt19937 gen(rd());

  std::uniform_real_distribution<float> dist(0, 19999);

  for (int i = 0; i < sampleSize; i++) {
    int randomNumber = dist(gen);

    while (true) {
      bool canExit = true;

      for (int j = 0; j < sample.size(); j++) {
        if (sample.at(j) == population.at(randomNumber)) {
          randomNumber = dist(gen);
          canExit = false;
          break;
        }
      }

      if (canExit) { break; }
    }

    sample.push_back(population.at(randomNumber));
  }
}

void Swap(float &a, float &b) {
  float temp = a;
  a = b;
  b = temp;
}

void BubbleSort(std::vector<float> &sample) {
  for (int i = 0; i < sample.size(); i++) {
    for (int j = 1; j < sample.size() - i; j++) {
      if (sample.at(j) > sample.at(j - 1)) {
        Swap(sample.at(j), sample.at(j - 1));
      }
    }
  }
}

#pragma region Merge Sort
void Merge(std::vector<float> &sample, int left, int mid, int right) {
  int n1 = mid - left + 1;
  int n2 = right - mid;

  std::vector<float> leftVector;
  std::vector<float> rightVector;

  for (int i = 0; i < n1; i++) {
    leftVector.push_back(sample.at(left + i));
  }

  for (int j = 0; j < n2; j++) {
    rightVector.push_back(sample.at(mid + 1 + j));
  }

  int i = 0;
  int j = 0;
  int k = left;

  while (i < n1 && j < n2) {
    if (leftVector.at(i) >= rightVector.at(j)) {
      sample.at(k) = leftVector.at(i);
      i++;
    }
    else {
      sample.at(k) = rightVector.at(j);
      j++;
    }

    k++;
  }

  while (i < n1) {
    sample.at(k) = leftVector.at(i);
    i++;
    k++;
  }

  while (j < n2) {
    sample.at(k) = rightVector.at(j);
    j++;
    k++;
  }
}

void MergeSort(std::vector<float> &sample, int left, int right) {
  if (left < right) {
    int mid = left + (right - left) / 2;

    MergeSort(sample, left, mid);
    MergeSort(sample, mid + 1, right);

    Merge(sample, left, mid, right);
  }
}
#pragma endregion


#pragma region Quick Sort
int Partition(std::vector<float> &sample, int low, int high) {
  float pivot = sample.at(high);

  int i = low - 1;

  for (int j = low; j < high; j++) {
    if (sample.at(j) >= pivot) {
      i++;
      Swap(sample.at(i), sample.at(j));
    }
  }

  Swap(sample.at(i + 1), sample.at(high));
  return i + 1;
}

void QuickSort(std::vector<float> &sample, int low, int high) {
  if (low < high) {
    int pivotIndex = Partition(sample, low, high);

    QuickSort(sample, low, pivotIndex - 1);
    QuickSort(sample, pivotIndex + 1, high);
  }
}
#pragma endregion

void RunBubbleSortAndShowResults(std::vector<float> sample, int sampleNumber, std::vector<std::string> &runTime) {
  std::vector<float> sortedSample = sample;

  auto startTimer = std::chrono::high_resolution_clock::now();
  BubbleSort(sortedSample);
  auto endTimer = std::chrono::high_resolution_clock::now();
  auto timerDuration = std::chrono::duration_cast<std::chrono::microseconds>(endTimer - startTimer);

  runTime.push_back(std::to_string(timerDuration.count()) + " microsegundos");

  // Print(sortedSample, sampleNumber);
  // std::cout << "Run time: " << runTime.at(0) << "\n" << std::endl;
}

void RunMergeSortAndShowResults(std::vector<float> sample, int sampleNumber, std::vector<std::string> &runTime) {
  std::vector<float> sortedSample = sample;

  auto startTimer = std::chrono::high_resolution_clock::now();
  MergeSort(sortedSample, 0, sortedSample.size() - 1);
  auto endTimer = std::chrono::high_resolution_clock::now();
  auto timerDuration = std::chrono::duration_cast<std::chrono::microseconds>(endTimer - startTimer);

  runTime.push_back(std::to_string(timerDuration.count()) + " microsegundos");

  // Print(sortedSample, sampleNumber);
  // std::cout << "Run time: " << runTime.at(1) << "\n" << std::endl;
}

void RunQuickSortAndShowResults(std::vector<float> sample, int sampleNumber, std::vector<std::string> &runTime) {
  std::vector<float> sortedSample = sample;

  auto startTimer = std::chrono::high_resolution_clock::now();
  QuickSort(sortedSample, 0, sortedSample.size() - 1);
  auto endTimer = std::chrono::high_resolution_clock::now();
  auto timerDuration = std::chrono::duration_cast<std::chrono::microseconds>(endTimer - startTimer);

  runTime.push_back(std::to_string(timerDuration.count()) + " microsegundos");

  // Print(sortedSample, sampleNumber);
  // std::cout << "Run time: " << runTime.at(2) << "\n" << std::endl;
}

void ExportToCSV(const std::vector<std::vector<std::string>> &data, const std::string &name) {
  std::ofstream csvFile(name, std::ios::app);

  if (csvFile.is_open()) {
    for (const auto &row : data) {
      for (size_t i = 0; i < row.size(); ++i) {
        csvFile << row.at(i);

        if (i < row.size() - 1) {
          csvFile << ",";
        }
      }

      csvFile << "\n";
    }

    csvFile.close();
  }
}

int GetCSVPos(const std::string &name) {
  std::vector<std::string> currentLine;

  std::ifstream csvFile(name);

  if (csvFile.is_open()) {

    std::string line;
    while (std::getline(csvFile, line)) {
      currentLine.push_back(line);
    }
  }

  csvFile.close();

  return currentLine.size();
}

int IsSpecsInCSV(const std::string &name, int &id, const std::string &so, const std::string &arquitetura, const std::string &tipo, const std::string &nucleos, const std::string &ram) {

  std::ifstream csvFile(name);
  int currentId = 0;

  if (csvFile.is_open()) {
    if (GetCSVPos(name) == 0) {
      csvFile.close();
      std::cout << "Configuracao nova\nAdicionando no arquivo...";
      return 0;
    }

    std::string csvCabecalho, csvId, csvSo, csvArquitetura, csvTipo, csvNucleos, csvRam;

    std::getline(csvFile, csvCabecalho);

    while (csvFile.good()) {
      std::string linha;
      getline(csvFile, linha);

      if (linha.empty()) {
        continue;
      }

      currentId++;

      std::stringstream ss(linha);

      getline(ss, csvId, ',');
      getline(ss, csvSo, ',');
      getline(ss, csvArquitetura, ',');
      getline(ss, csvTipo, ',');
      getline(ss, csvNucleos, ',');
      getline(ss, csvRam);

      if (csvSo == so && csvArquitetura == arquitetura && csvTipo == tipo && csvNucleos == nucleos && csvRam == ram) {
        csvFile.close();
        id = currentId;
        std::cout << "Configuracao ja existente na linha " << id << "\n";
        return 1;
      }
    }
  }
  csvFile.close();

  id = GetCSVPos(name);
  std::cout << "Configuracao nova detectada\nAdicionando no arquivo... \n";
  return 0;
}