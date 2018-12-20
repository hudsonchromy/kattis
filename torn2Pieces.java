import java.util.*;

public class torn2Pieces {

   

   public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      String[] line;
      Set<String> visited = new HashSet<String>();
      HashMap<String, Set<String>> map = new HashMap<>();
      HashMap<String, String> pathTracing = new HashMap<>();
      Queue<String> q = new LinkedList<>();
      String curr, last;
      
      int pieces = Integer.parseInt(input.nextLine());
      for(int i = 0; i < pieces; i++) {
         line = input.nextLine().split(" ");
         if(!map.containsKey(line[0])) {
            Set<String> empty = new HashSet<String>();
            map.put(line[0], empty);
         }
         for(int j = 1; j < line.length; j++) {
            map.get(line[0]).add(line[j]);
            if(!map.containsKey(line[j])) {
               Set<String> empty = new HashSet<String>();
               map.put(line[j], empty);
            }
            map.get(line[j]).add(line[0]);
         }
      }
      //System.out.println(map);
      line = input.nextLine().split(" ");
      String start = line[0];
      String end = line[1];
      last = start;
      q.add(start);
      String[] outp = {end};
      /////////////       BFS       /////////////////
      pathTracing.put(start, start);
      while(true){
         if(q.size() == 0) {
            outp[0] = "no route found";
            break;
         }
         curr = q.poll();
         visited.add(curr);
         //pathTracing.put(curr, last);
         if(curr.equals(end)) {
            //System.out.println(pathTracing);
            while(!outp[outp.length-1].equals(start)) {
               outp = Arrays.copyOf(outp, outp.length + 1);
               outp[outp.length-1] = pathTracing.get(outp[outp.length-2]);
            }
            break;
         }
         Set<String> neighbors = map.get(curr);
         if(neighbors != null) {
			   for(String node: neighbors) {
			     	if(!visited.contains(node)) {
					   q.add(node);
					   pathTracing.put(node, curr);
				   }
			   }
		   }
      }
      //System.out.println(pathTracing);
      for(int i = outp.length-1; i > 0; i--) {
         System.out.print(outp[i]);
         System.out.print(" ");
      }
      System.out.println(outp[0]);
   }
}
