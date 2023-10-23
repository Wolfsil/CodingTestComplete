using System;
using System.Collections.Generic;
namespace Program
{
    public class collections
    {
        public class test
        {
            public int id = 0;
            public test(int id)
            {
                this.id = id;
            }
        }
        void list() { 
            List<test> l=new List<test>();
            l.Add(new test(3));
            l.Add(new test(2));
            l.Add(new test(1));
            l.Add(new test(4));
            l.Add(new test(3));
            l.Add(new test(2));
            l.Add(new test(1));
            l.Add(new test(4));
            for (int i = 0; i < l.Count; i++)
            {
                l[i] = l[i];
                Console.WriteLine(l[i].id);
                
            }
            for (int i = 0; i < l.Count; i++)
            {
                l.Remove(l[i]);
            }//==l.RemoveAll()


        }
        void diction()
        {
            Dictionary<string, test> dic = new Dictionary<string, test>();
            dic["일"] = new test(1);
            dic["이"] = new test(2);
            dic["삼"] = new test(3);

            foreach(string key in dic.Keys)
            {
                Console.WriteLine(key);
            }
            dic.Remove("일");
            foreach (string key in dic.Keys)
            {
                Console.WriteLine(key);
            }

        }

        void QuStac()
        {
            Console.WriteLine("queue");
            Queue<test> q = new Queue<test>();
            q.Enqueue(new test(1));
            q.Enqueue(new test(2));
            q.Enqueue(new test(3));
            Console.WriteLine(q.Dequeue().id);
            Console.WriteLine("stack");
            Stack<test> s = new Stack<test>();
            s.Push(new test(1));
            s.Push(new test(2));
            s.Push(new test(3));
            Console.WriteLine(s.Pop().id);
        }


        public static void Mains(string[] args)
        {
            collections co=new collections();
            co.list();

        }

    }


}