using System;

namespace Program
{
    public class develop
    {
        public static int[] solution(int[] progresses, int[] speeds)
        {
            int[] answer = new int[100];
            int[] realAnswer;
            int answerCount = 0;

            for (int i = 0; i < progresses.Length;)
            {
                int count = 0;
                int day = (int)Math.Ceiling((100.0 - progresses[i]) / speeds[i]);
                bool flag = true;

                for (int j = i; j < progresses.Length; j++)
                {
                    progresses[j] += speeds[j] * day;
                    Console.WriteLine(progresses[j]);
                    if (progresses[j]>= 100 && flag)
                    {
                        count++;
                    }
                    else
                    {
                        flag = false;
                    }                
                }
               
                answer[answerCount++] = count;
                i += count;
            }


            realAnswer = new int[answerCount];
            for (int i = 0; i < answerCount; i++)
            {
                realAnswer[i] = answer[i];
                Console.WriteLine(realAnswer[i]);
               
            }

            return realAnswer;
        }
        public static void Mains(string[] args)
        {

            solution(new int[]{ 9,9,9} ,new int[] { 9,9,9 });

        }

    }


}