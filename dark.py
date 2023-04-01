import urllib.request
import tkinter as tk
import time

def test_connectivity():
  window = tk.Tk()
  window.title("Website Connectivity Checker")
  window.geometry('600x200')
  window.resizable(False, False)
  window.configure(bg="#1c1c1c")
  head = tk.Label(window, text='Enter the URL of the Website', font=('Space Mono', '15'), bg='#1c1c1c', fg='#f0f0f0')
  head.pack(pady=15)

  def im():
     tk.Label(window, text='                                     ', font=('Space Mono', '20'), fg="#1c1c1c", bg='#1c1c1c').place(x=170, y=140)

  def check_url():
      web = (url.get())
      status_code = urllib.request.urlopen(web).getcode()
      website_is_up = status_code == 200
      if website_is_up:
          tk.Label(window, text='WEBSITE AVAILABLE', font=('Space Mono', '20'), fg="green", bg='#1c1c1c').place(x=170, y=140)
      else:
          tk.Label(window, text='WEBSITE NOT AVAILABLE', font=('Space Mono', '20'), fg="red", bg='#1c1c1c').place(x=140, y=140)

  url=tk.StringVar()
  Entryy=tk.Entry(window, textvariable=url, font=('Space Mono', 12), bg='#1c1c1c', fg='#f0f0f0')
  Entryy.place(x=160, y=55, height=30, width=280)
  Entryy.bind("<Return>", lambda x: check_url())
  Entryy.bind('<Key>', lambda y: im())
  Entryy.insert('end', 'https://')
  tk.Button(window, text='Check', command=check_url, font=('Space Mono', '12'), bg='#1c1c1c', fg='#f0f0f0').place(x=265, y=95)
  window.mainloop()


if __name__ == '__main__':
  test_connectivity()
