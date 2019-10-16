public class Prob_8 {
	public static void main(String[] args) {
		int Y = 0;
		int X = (Y + 4) * 3;
	}
}
/*
Compiled from "Prob_8.java"
public class Prob_8 {
  public Prob_8();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: iconst_0	//把0放到栈顶
       1: istore_1	//把栈顶值0放到1中，即i中
       2: iload_1	//把i的值放到栈顶，0
       3: iconst_4	//把4放到栈顶
       4: iadd		//栈顶4+0放到栈顶
       5: iconst_3	//把3放到栈顶
       6: imul		//栈顶4*3放到栈顶
       7: istore_2	//把栈顶值12放到1中，即i中
       8: return
}
*/