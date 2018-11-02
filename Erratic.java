import java.util.*;
import java.io.*;

public class Erratic {
   static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
   
   static final int NORTH = 0;
   static final int EAST = 1;
   static final int SOUTH = 2;
   static final int WEST = 3;
   
   static final int START = 60;
   
   static boolean[][] visited = new boolean[121][121];
   static boolean[][][] canMove = new boolean[121][121][4];
   static Queue<Integer> xQueue = new LinkedList<Integer>();
   static Queue<Integer> yQueue = new LinkedList<Integer>();
   
   public static void main(String args[]) throws IOException {

      //System.out.println(Arrays.toString(canMove[60][60]));
      int line = Integer.valueOf(input.readLine());
      //System.out.println(line);
      StringBuilder sb = new StringBuilder();
      while(line-- > 0) {
         //System.out.println("Start");
         input.readLine();
         reset();
         int maxSteps = Integer.valueOf(input.readLine());
         //System.out.println(maxSteps);
         int x = START, y = START;
         for (int i = 0; i < maxSteps; i++) {
            char move = input.readLine().charAt(0);
            int dir = getDir(move);
            canMove[y][x][dir] = true;
            
            x += getXMove(dir);
            y += getYMove(dir);
            
            int oppisiteDir = oppisiteDirection(dir);
            canMove[y][x][oppisiteDir] = true;
         }
         //System.out.println(Arrays.toString(canMove[60][60]));
         //System.out.println(x);
         //System.out.println(y);
         //System.out.println(directions); 
         System.out.println(bfs(START, START, x, y));
      }
   }
   
   static int getXMove(int dir) {
      switch(dir) {
         case NORTH:
         case SOUTH:
            return 0;
         case WEST:
            return -1;
         default:
            return 1;    
      }
   }
   
   
   static int bfs(int startX, int startY, int endX, int endY) {
      xQueue.offer(startX);
      yQueue.offer(startY);
      xQueue.offer(null);
      int depth = 0;
      while(true) {
         if(xQueue.peek() == null) {
            xQueue.offer(xQueue.poll());
            depth++;
         }
         else {
            int x = xQueue.poll();
            int y = yQueue.poll();
            if(x == endX && y == endY) {
               return depth;
            }
            for(int dir = 0; dir < 4; dir++) {
               if(canMove[y][x][dir]) {
                  int newX = x + getXMove(dir);
                  int newY = y + getYMove(dir);
                  if(!visited[newY][newX]) {
                     xQueue.offer(newX);
                     yQueue.offer(newY);
                     visited[newY][newX] = true;
                  }
               }
            }
         }
      }
   }
   
   
   
   static int getYMove(int dir) {
      switch(dir) {
         case EAST:
         case WEST:
            return 0;
         case NORTH:
            return -1;
         default:
            return 1;    
      }
   }
   
   static int oppisiteDirection(int dir) {
      switch(dir) {
         case NORTH:
            return SOUTH;
         case SOUTH:
            return NORTH;
         case EAST:
            return WEST;
         default:
            return EAST;
      }
   }
   
   static int getDir(char ch) {
      switch(ch) {
         case 'N':
            return NORTH;
         case 'E':
            return EAST;
         case 'S':
            return SOUTH;
         default:
            return WEST;
      }
   }
   
   static void reset() {
      xQueue.clear();
      yQueue.clear();
      for (int i = 0; i < 121; i++) {
         Arrays.fill(visited[i], false);
         for (int j = 0; j < 121; j++) {
            Arrays.fill(canMove[i][j], false);
         }
      }
   }
   
}