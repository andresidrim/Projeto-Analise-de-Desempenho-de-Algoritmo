#pragma once

#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <string>
#include <fstream>

#ifdef _WIN32
#include <Windows.h>

void GetWindowsHardwareInfo() {
  SYSTEM_INFO sysInfo;
  GetSystemInfo(&sysInfo);

  switch (sysInfo.wProcessorArchitecture) {
  case PROCESSOR_ARCHITECTURE_AMD64:
    std::cout << "AMD x64\n";
    break;
  case PROCESSOR_ARCHITECTURE_INTEL:
    std::cout << "INTEL x86\n";
    break;
  default:
    std::cout << "Unknown\n";
  }
}

#elif __APPLE__
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