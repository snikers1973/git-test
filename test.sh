#!/bin/bash

# Функция для получения размера файла или директории
get_size() {
    local path="$1"
    if [ -f "$path" ]; then
        # Если это файл, используем stat для получения размера
        stat --format="%s" "$path" 2>/dev/null || echo "Ошибка при чтении файла $path"
    elif [ -d "$path" ]; then
        # Если это директория, используем du для получения размера
        du -sb "$path" 2>/dev/null | cut -f1 || echo "Ошибка при доступе к директории $path"
    else
        echo 0
    fi
}

# Функция для анализа размеров в текущей директории
analyze_sizes() {
    local items=(*)
    local sizes=()

    for item in "${items[@]}"; do
        if [ -e "$item" ]; then
            size=$(get_size "$item")
            sizes+=("$size $item")
        fi
    done

    # Сортировка по убыванию размера
    IFS=$'\n' sorted=($(sort -rn <<<"${sizes[*]}"))
    unset IFS

    # Вывод результатов
    for entry in "${sorted[@]}"; do
        echo "$entry bytes"
    done
}

# Запуск функции анализа
analyze_sizes
