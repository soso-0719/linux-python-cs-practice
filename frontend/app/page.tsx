"use client";

import { useEffect, useState } from "react";
import type { FormEvent } from "react";

type StudyLog = {
  id: number;
  title: string;
  minutes: number;
  created_at: string;
};

type LogsResponse = {
  logs: StudyLog[];
};
// React component
// src/app/page.txtがページになる。
export default function Home() {

  //Reactだとlet logs = [];
  //logs = data.logs;
  //としても、Reactは自動で画面を描き直してくれない
  const [logs, setLogs] = useState<StudyLog[]>([]);
  //Reactが内部のコンポーネント情報管理のためにuseStateを使っている。
  //logsにはStudylogの型の配列のみ入る
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [title, setTitle] = useState("");
  const [minutes, setMinutes] = useState("");
  //setlogsはuseState は内部的に、こういう2つ返す。
  //[現在の値, 更新するための関数]
  //今回なら、[logs, setLogs]に分けて受け取っている。
  const totalMinutes = logs.reduce((total, log) => {
    return total + log.minutes;
  }, 0);
  const API_BASE_URL = "http://127.0.0.1:5000";
  //バックエンド側のルート

  //GET
  //ReactはuseEffect(async () => { ...}, []);
  // useEffect の関数自体を async（こいつでawait使えるようになる） にするのは基本避けるべきらしい。
  async function fetchLogs() {
    try {
      //GET リクエスト
      const response = await fetch(`${API_BASE_URL}/study-logs`);
      //responseにはHTTPレスポンス全体が入ってる
      if (!response.ok) {
        throw new Error("Failed to fetch from study logs");
      }

      const data: LogsResponse = await response.json();//bodyにあるjson返す
      setLogs(data.logs);
      // logs stateを更新する。Reactは再描画のためにHomeを再実行してる。
    } catch {
      setError("Network error. Please check the Flask API server.");
    } finally {
      setLoading(false);
    }
  }
  //画面が表示されたあとに1回だけやりたい処理
  useEffect(() => {
    fetchLogs();
  }, []);
  //POST
  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    //event は、フォーム送信が起きた時のイベント情報
    //preventDefaultはHTML標準のフォームの送信を止める。
    //ようはStateがリロードされないようにする
    setError("");

    try {
      const response = await fetch(`${API_BASE_URL}/study-logs`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title,
          minutes: minutes,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.error || "Failed to add study log");
        return;
      }

      setTitle("");
      setMinutes("");

      await fetchLogs();
    } catch {
      setError("Network error. Please check the Flask API server.");
    }
  }
  //DELETE
  async function handleDelete(id: number) {
    setError("");

    try {
      const response = await fetch(`${API_BASE_URL}/study-logs/${id}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        setError("Failed to delete study log");
        return;
      }

      await fetchLogs();
    } catch {
      setError("Network error. Please check the Flask API server.");
    }
  }
  return (
    <main>
      <h1>Study Log App</h1>
      <p>Flask API and SQLite practice with Next.js frontend.</p>

      <section>
        <h2>Summary</h2>
        <p>Total Minutes: {totalMinutes}</p>
        <p>Total Logs: {logs.length}</p>
      </section>

      <section>
        <h2>Add Study Log</h2>

        <form onSubmit={handleSubmit}>
          <input
            placeholder="Title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
          />

          <input
            placeholder="Minutes"
            value={minutes}
            onChange={(event) => setMinutes(event.target.value)}
          />

          <button type="submit">Add</button>
        </form>
      </section>

      <section>
        <h2>Recent Logs</h2>

        {loading && <p>Loading study logs...</p>}

        {error && <p>{error}</p>}

        {!loading && !error && logs.length === 0 && (
          <p>No study logs yet.</p>
        )}

        {!loading && !error && logs.length > 0 && (
          <div>
            {logs.map((log) => (
              <div key={log.id}>
                <p>Title: {log.title}</p>
                <p>Minutes: {log.minutes}</p>
                <p>Created At: {log.created_at}</p>

                <button onClick={() => handleDelete(log.id)}>Delete</button>
              </div>
            ))}
          </div>
        )}
      </section>
    </main>
  );
}