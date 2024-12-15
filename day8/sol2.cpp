#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>

struct Coordinate {
	int row;
	int col;

	std::string display() {
		return std::to_string(row) + "x" + std::to_string(col);
	}

	Coordinate operator + (const Coordinate &other) {
		Coordinate result;
		result.row = row + other.row;
		result.col = col + other.col;
		return result;
	}

	Coordinate operator - (const Coordinate &other) {
		Coordinate result;
        result.row = row - other.row;
        result.col = col - other.col;
        return result;
	}

	bool operator == (const Coordinate &other) const {
		return row == other.row && col == other.col;
	}
};

void showLines(std::vector< std::vector<char> > lines);
std::string asciiLowercase();
std::string asciiUppercase();
std::unordered_map<char, std::vector<Coordinate> > getSignPositions(
	std::vector< std::vector<char> > board,
	std::string signsToSearch
);
void showMap(std::unordered_map<char, std::vector<Coordinate> > map);
void drawAntinodes(
	std::vector< std::vector<char> > *board,
	std::unordered_map<char, std::vector<Coordinate> > &signPositions
);
long int countValues(std::vector< std::vector<char> > board, char signToCount);


int main() {
	std::fstream inputFile("input1.txt");
	std::string newLine;
	std::vector< std::vector<char> > board;
	while (inputFile >> newLine) {
		std::vector<char> line;
		for (char i : newLine) {
			line.push_back(i);
		}
		board.push_back(line);
	}
	showLines(board);

	std::string signsToSearch = "0123456789";
	signsToSearch += asciiLowercase();
	signsToSearch += asciiUppercase();
	std::cout << signsToSearch << "\n";
	std::unordered_map<char, std::vector<Coordinate> > signPositions = getSignPositions(board, signsToSearch);
	showMap(signPositions);
	drawAntinodes(&board, signPositions);
	showLines(board);
	std::cout << countValues(board, '#') << std::endl;
}

void showLines(std::vector< std::vector<char> > lines) {
	for (auto line : lines) {
		for(auto sign : line) {
			std::cout << sign;
		}
		std::cout << "\n";
	}
}

void showCoordinates(std::vector<Coordinate> coordinates) {
	for (Coordinate i : coordinates) {
		std::cout << i.display() << " ";
	}
	std::cout << "\n";
}

void showMap(std::unordered_map<char, std::vector<Coordinate> > map) {
	for (auto i = map.begin(); i != map.end(); i++) {
		std::cout << i->first << "\t";
		showCoordinates(i->second);
	}
	std::cout << "\n";
}

void drawAntinodes(
	std::vector< std::vector<char> > *board,
	std::unordered_map<char, std::vector<Coordinate> > &signPositions
) {
	int maxRows = board->size();
	int maxCols = (*board)[0].size();
	for (auto i = signPositions.begin(); i != signPositions.end(); i++) {
		for (Coordinate firstCoord : i->second) {
			for (Coordinate secondCoord : i->second) {
				if (firstCoord == secondCoord) {
					continue;
				}
				Coordinate diff = firstCoord - secondCoord;
				Coordinate current = firstCoord;
				Coordinate antinodeCoord;
				while (true) {
					antinodeCoord = current + diff;
					if (antinodeCoord.row < 0 || antinodeCoord.col < 0
                    	|| antinodeCoord.row >= maxRows || antinodeCoord.col >= maxCols) {
						break;
					}
					(*board)[antinodeCoord.row][antinodeCoord.col] = '#';
					current = antinodeCoord;
				}
				current = secondCoord;
				while (true) {
					Coordinate antinodeCoord = current - diff;
					if (antinodeCoord.row < 0 || antinodeCoord.col < 0
                    	|| antinodeCoord.row >= maxRows || antinodeCoord.col >= maxCols) {
						std::cout << antinodeCoord.display() << "\n";
                    	break;
                    }
                    (*board)[antinodeCoord.row][antinodeCoord.col] = '#';
					current = antinodeCoord;
				}
			}
		}
	}
}


long int countValues(std::vector< std::vector<char> > board, char signToCount) {
	long int count = 0;
	for (auto row : board) {
		for (auto sign : row) {
			count += sign != '.';
		}
	}
	return count;
}

std::string asciiLowercase() {
    std::string result;
	for (char c = 'a'; c <= 'z'; ++c) {
        result += c;
	}
    return result;
}

std::string asciiUppercase() {
	std::string result;
	for (char c = 'A'; c <= 'Z'; ++c) {
	    result += c;
	}
	return result;
}

// Getting {letter: [(x, y)]}
std::unordered_map<char, std::vector<Coordinate> > getSignPositions(
	std::vector< std::vector<char> > board,
	std::string signsToSearch
) {
	std::unordered_map< char, std::vector<Coordinate> > signPositions;
	for (int row = 0; row != board.size(); row++) {
		for (int col = 0; col != board[row].size(); col++) {
			if (!(signsToSearch.find(board[row][col]) < signsToSearch.length())) {
				continue;
			}
			signPositions[board[row][col]].push_back({ row, col });
		}
	}
	return signPositions;
}

