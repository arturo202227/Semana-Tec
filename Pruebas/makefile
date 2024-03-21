CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRCS = hello.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = hello

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

.cpp.o:
	$(CXX) $(CXXFLAGS) -c $<

clean:
	$(RM) $(OBJS) $(TARGET)