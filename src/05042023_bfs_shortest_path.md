## Algorithm Problem Solving Workout
**05/04/2023**


### Q1: Get all numbers from a string
- input: a string, could be **null**
- output: a list of numbers(string)
- come at least two methods to solve this problem.

#### Solution:
- High Level:
  > Enumerate each char, if its digit, we got the start, use two point to find the end. Add it to result, then recursion to next one.
  > if its not digit, we skip it.

- Algorithm Knowledge:
  > practice recursion

- Code Tricks:
  > As long as we handle some rules of string,
  > we could think of regex first.

#### Code:
```python
# find all numbers in a string
def get_all_numbers(input_str):
  res = []
  n = len(input_str)
  # enumeratre each char in the string
  def dfs(i):
    # base case
    if i == n:
      return
    # branch I: operation for char is digit 
    if input_str[i].isdigit():
      j = i
      while j < n and input_str[j].isdigit():
        j += 1
      res.append(input_str[i:j])
      dfs(j)
    # operation for char is not digit
    else:
      # branch II: skip the char
      dfs(i+1)
  # start from the first char
  dfs(0)
  return res

test_str = "abc 112def 454 445 889 afef33 4"
print(get_all_numbers(test_str))
```

```python
import re 

# use regex
text = "abc 112def 454 445 889 afef33 4"
print(re.findall(r'\d+', text))
```

```java
import java.util.ArrayList;

public class StringNumbers {
    
    public static ArrayList<String> getAllNumbers(String inputStr) {
        ArrayList<String> res = new ArrayList<>();
        int n = inputStr.length();
        
        // define dfs function (inner recursive function)
        dfs:
        for (int i=0; i<n; i++) {
            // branch I: operation for char is digit 
            if (Character.isDigit(inputStr.charAt(i)) || inputStr.charAt(i) == '-') {
                int j = i;
                while (j < n && (Character.isDigit(inputStr.charAt(j)) || inputStr.charAt(j) == '.')) {
                    j++;
                }
                res.add(inputStr.substring(i, j));
                i = j;
            }
            // operation for char is not digit
            else {
                // branch II: skip the char
                continue dfs;
            }
        }
        
        return res;
    }
    
    public static void main(String[] args) {
        String testStr = "The quick -12.45 brown 6.7 fox 5 jumps over the lazy dog.";
        ArrayList<String> numList = getAllNumbers(testStr);
        System.out.println(numList);
        // output: [-12.45, 6.7, 5]
    }

}

```

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        String text = "abc 112def 454 445 889 afef33 4";
        Pattern pattern = Pattern.compile("\\d+");
        Matcher matcher = pattern.matcher(text);
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}

```

### [Q2] -  Shortest Cycle in a Graph

#### Solution:
- High Level:
  > Define the cycle, if a node is visited by different  path at the first time, it means we find a cycle.
  > We could enumerate each node as start point, to find the first cycle, which its the shortest cycle.

- Algorithm Knowledge:
  > If the weight of edge is 1, we can use BFS to find the shortest path. 

- Code Tricks:
  > init dist[n] with -1, to mark the first visit.
  > use pair (node, father) to differentiate the paths.

#### Code:

```python
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # build graph

        def bfs(start: int) -> int:
            ans = inf
            dis = [-1] * n  # dis[i] the shortest distance of start->i
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # first time visit
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # second time, got a cycle
                        ans = min(ans, dis[x] + dis[y] + 1)
            return ans

      ans = min(bfs(i) for i in rang(n))
      return ans if ans < inf else -1
```

#### Java

```java
class Solution {
    private List<Integer>[] g;
    private int[] dis;

    public int findShortestCycle(int n, int[][] edges) {
        // build the graph
        g = new ArrayList[n]; // new int[n]
        Arrays.setAll(g, e -> new ArrayList<Integer>());
        for(var e: edges) {
            int x = e[0], y = e[1];
            g[x].add(y);
            g[y].add(x);
        }
        dis = new int[n];
        int ans = Integer.MAX_VALUE;
        // enumerate each node as start point
        for (int i = 0; i < n; ++i) 
            ans = Math.min(ans, bfs(i));
        return ans < Integer.MAX_VALUE ? ans : -1;
    }

    private int bfs(int start) {
        int ans = Integer.MAX_VALUE;
        Arrays.fill(dis, -1);
        // remember its father node
        var q = new ArrayDeque<int[]>();
        q.add(new int[]{start, -1});
        dis[start] = 0;

        while (!q.isEmpty()) {
            var p = q.poll();
            int x = p[0], fa = p[1];
            for (var y: g[x]) {
                if (dis[y] < 0) { // first time visit
                    dis[y] = dis[x] + 1;
                    q.add(new int[]{y, x});
                } else if (y != fa) {  // second time visit, got a cycle
                    ans = Math.min(ans, dis[x] + dis[y] + 1);
                }
            }
        }
        return ans;
    }
}
```

##### Homework:
- finish Q1 in Java.
- Code Q2 and understand BFS shortest path and coding tricks.

## Go
**Go! Grow together**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO -     http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Q2]: <https://leetcode.cn/problems/shortest-cycle-in-a-graph/>